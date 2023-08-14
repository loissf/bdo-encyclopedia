import axios from "axios";
import fs from "fs";

// map all icons with id from 0 to 100000 from arsha.io api
async function map() {
  let results = [];
  const successes: number[] = [];
  const failures: number[] = [];
  for (let i = 0; i < 100000; i++) {
    const result = axios.get(`https:\\cdn.arsha.io/icons/${i}.png`);

    result
      .then(() => {
        successes.push(i);
      })
      .catch(() => {
        failures.push(i);
      });

    results.push(result);

    if (i % 100 === 0) {
      await Promise.allSettled(results);
      results = [];
    }
  }

  Promise.allSettled(results).then(() => {
    console.log("success", successes);
    console.log("failures", failures);
  });

  fs.writeFile("successes.json", JSON.stringify(successes), (error) => {
    if (error) {
      console.error(error);

      throw error;
    }
  });
  fs.writeFile("failures.json", JSON.stringify(failures), (error) => {
    if (error) {
      console.error(error);

      throw error;
    }
  });
}
