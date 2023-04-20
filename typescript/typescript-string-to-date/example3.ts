// https://codevscolor.com/typescript-string-to-date

import { parse } from "date-fns";

const strDate = "04-04-2023";

const date = parse(strDate, "dd-MM-yyyy", new Date());

console.log(`Date: ${date.toISOString()}`);