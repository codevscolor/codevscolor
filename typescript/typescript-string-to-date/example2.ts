// https://codevscolor.com/typescript-string-to-date

import moment from "moment";

const strDate = "14-04-2023 03:02:03";

const date = moment(strDate, "DD-MM-yyyy hh:mm:ss").toDate();

console.log(`Date: ${date}`);