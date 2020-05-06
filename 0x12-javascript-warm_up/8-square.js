#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  for (let i = 0; i < size; ++i) {
    let j = 0;

    for (; j < size; ++j) {
      process.stdout.write('X');
    }

    if (j === size) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
