import chai from 'chai';
import kue from 'kue';
import { createPushNotificationsJobs } from './8-job';

const { expect } = chai;

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient(), prefix: 'test' } });
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient(), prefix: 'test' } });
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidCall = () => createPushNotificationsJobs('invalid', queue);
    expect(invalidCall).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);

    jobs.forEach((jobData, index) => {
      const queueJob = queue.testMode.jobs[index];
      expect(queueJob.type).to.equal('push_notification_code_3');
      expect(queueJob.data).to.deep.equal(jobData);
    });
  });
});

