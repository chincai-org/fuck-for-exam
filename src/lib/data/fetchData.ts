import bank from "./bank.json";
import definitions from "./definitions.json";
import questions from "./questions.json";
import type { Question, Result } from "./types";

const definitionsDict: { [key: string]: any } = definitions;
const questionsDict: { [key: string]: Question } = questions;

export function getDefinition(lang: any, word: any) {
    return definitionsDict[lang][word];
}

export function findData(query: string | undefined, data: Array<Result | string | any> = bank) {
    if (!query) return data as Array<Result>;

    let result: Result = data.find((item: any) => item.id === query) || {};

    return result.childs as Array<Result | string>;
}

export function recursiveFind(routeList: Array<string>, data: Array<Result | string | any> = bank) {
    let currentData = findData(routeList.shift(), data);

    if (routeList.length === 0) return currentData;

    return recursiveFind(routeList, currentData);
}

export function getQuestion(id: string) {
    return questionsDict[id];
}
