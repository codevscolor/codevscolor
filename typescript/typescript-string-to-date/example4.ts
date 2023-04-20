// https://codevscolor.com/typescript-string-to-date

import { parse } from "date-fns";

const strDate = "14-04-2023 03:02:03+00";

const date = parse(strDate, "dd-MM-yyyy hh:mm:ssx", new Date());

console.log(`Date: ${date.toISOString()}`);
