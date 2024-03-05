import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0715813670',
  message: 'Hello, this is a notification!',
};

const notificationJob = queue.create('push_notification_code', jobData);

notificationJob.on('enqueue', () => {
  console.log(`Notification job created: ${notificationJob.id}`);
  process.exit(0);
});

notificationJob.on('complete', () => {
  console.log('Notification job completed');
  process.exit(0);
});

notificationJob.on('failed', () => {
  console.log('Notification job failed');
  process.exit(1);
});

notificationJob.save();
