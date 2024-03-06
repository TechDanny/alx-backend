const express = require('express');
const redis = require('redis');
const kue = require('kue');

const { promisify } = require('util');

const app = express();
const port = 1245;

const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

const queue = kue.createQueue();

const initialAvailableSeats = 50;
let numberOfAvailableSeats = initialAvailableSeats;

let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const currentSeats = await getAsync('available_seats');
  return currentSeats ? parseInt(currentSeats) : 0;
}

app.get('/available_seats', (req, res) => {
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats > 0) {
    numberOfAvailableSeats = currentAvailableSeats - 1;
    await reserveSeat(numberOfAvailableSeats);

    if (numberOfAvailableSeats === 0) {
      reservationEnabled = false;
    }
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
