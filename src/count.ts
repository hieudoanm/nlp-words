import { readdirSync, writeFileSync } from 'fs';

const main = async () => {
  const files = readdirSync('./data');
  console.log(files.length);

  const markdown = `# Words (${files.length})

From [WordsAPI](https://www.wordsapi.com/)
`;

  writeFileSync('./README.md', markdown);

  process.exit(0);
};

main().catch((error) => console.error(error));
