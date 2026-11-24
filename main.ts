// news-image-20261123 — entry program (Node 22, standard library only).
//
// The front page lives in this repository as entry.png (drawn by
// draw.py, 1024x1024, 153662 bytes). The grader runs this program in a
// sandbox with no network: it reads the image from the repository and
// writes the same bytes to $MAKEFUN_OUTPUT_DIR/entry.png, which the
// grader then gates and shows to the judge.
//
// Usage outside the grader:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const sourceImage = join(repoRoot, "entry.png");

const outputDir = resolve(process.env.MAKEFUN_OUTPUT_DIR ?? "/output");
const targetImage = join(outputDir, "entry.png");

if (!existsSync(sourceImage)) {
  console.error(`missing image in repository: ${sourceImage}`);
  process.exit(1);
}

const pngBytes = readFileSync(sourceImage);
if (pngBytes.length === 0 || pngBytes.length > 1048576) {
  console.error(`entry.png has an unexpected size: ${pngBytes.length} bytes`);
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
writeFileSync(targetImage, pngBytes);

const written = readFileSync(targetImage);
if (!written.equals(pngBytes)) {
  console.error("verification failed: output bytes differ from entry.png");
  process.exit(1);
}

console.log(`wrote ${targetImage} (${written.length} bytes)`);
