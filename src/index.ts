import axios from 'axios';
import dotenv from 'dotenv';
import { existsSync, readFileSync, writeFileSync } from 'fs';

dotenv.config();

const ENCRYPTED = process.env.ENCRYPTED || '';
const LEVEL = process.env.LEVEL || '';
const WHEN = process.env.WHEN || '';

type Result = {
  synonyms: string[];
  typeOf: string[];
  hasTypes: string[];
  derivation: string[];
  similarTo: string[];
  regionOf: string[];
  instanceOf: string[];
  memberOf: string[];
  hasParts: string[];
  partOf: string[];
};

type Data = { word: string; results: Result[] };

const exportWord = async (filePath: string, data: Data) => {
  const content = JSON.stringify(data, null, 2);
  writeFileSync(filePath, content);
};

const getWord = async (queryWord: string) => {
  const fileName = queryWord.replace(/ /g, '-').toLowerCase();
  const filePath = `./data/${fileName}.json`;
  const exists = await existsSync(filePath);
  if (exists) return;
  try {
    const url = `https://www.wordsapi.com/mashape/words/${queryWord}?when=${WHEN}&encrypted=${ENCRYPTED}`;
    console.log(queryWord, url);
    const response: { data: Data } = await axios.get<Data>(url, {});
    const { data } = response;
    await exportWord(filePath, data);
    // const { results = [] } = data;
    // for (const result of results) {
    //   const {
    //     synonyms = [],
    //     typeOf = [],
    //     hasTypes = [],
    //     similarTo = [],
    //     regionOf = [],
    //     instanceOf = [],
    //     memberOf = [],
    //     hasParts = [],
    //     partOf = [],
    //   } = result;
    //   for (const synonym of synonyms) {
    //     await getWord(synonym);
    //   }
    //   for (const typeOfWord of typeOf) {
    //     await getWord(typeOfWord);
    //   }
    //   for (const hasType of hasTypes) {
    //     await getWord(hasType);
    //   }
    //   for (const similarWord of similarTo) {
    //     await getWord(similarWord);
    //   }
    //   for (const regionOfWord of regionOf) {
    //     await getWord(regionOfWord);
    //   }
    //   for (const instanceOfWord of instanceOf) {
    //     await getWord(instanceOfWord);
    //   }
    //   for (const memberOfWord of memberOf) {
    //     await getWord(memberOfWord);
    //   }
    //   for (const hasPart of hasParts) {
    //     await getWord(hasPart);
    //   }
    //   for (const partOfWord of partOf) {
    //     await getWord(partOfWord);
    //   }
    // }
  } catch (error) {
    console.error(error);
  }
};

const main = async () => {
  const wordsString: string = await readFileSync('./src/words.txt', 'utf-8');
  const length = 50000;
  const start = parseInt(LEVEL, 0) * 50000;
  const words: string[] = wordsString
    .split('\n')
    .slice(start, start + length)
    .reverse();
  for (const word of words) {
    await getWord(word.toLowerCase());
  }
};

main().catch((error) => console.error(error));
