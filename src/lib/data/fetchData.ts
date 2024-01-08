import bank from "./bank.json";
import definitions from "./definitions.json";
import type { Result } from "./types";

const definitionsDict: { [key: string]: any } = definitions;

export function getDefinition(lang: any, word: any) {
    return definitionsDict[lang][word];
}

export function findData(query: string | undefined, data: Array<Result | Object> = bank) {
    console.log(data);
    console.log(query);

    if (!query) return data as Array<Result>;

    let result: Result = data.find((item: any) => item.route === query) || {};
    console.log(result);
    return result.childs as Array<Result>;
}

export function recursiveFind(routeList: Array<string>, data: Array<Object> = bank) {
    console.log(routeList);

    let currentData = findData(routeList.shift(), data);
    console.log(currentData);

    if (routeList.length === 0) return currentData;

    return recursiveFind(routeList, currentData);
}
