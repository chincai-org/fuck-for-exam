import bank from "./bank.json";
import definitions from "./definitions.json";

const definitionsDict: { [key: string]: any } = definitions;

interface Result {
    route?: string;
    title?: string;
    childs?: Array<Result>;
}

export function getDefinition(lang: any, word: any) {
    return definitionsDict[lang][word];
}

export function findData(query: string | undefined, data: Array<Object> = bank) {
    console.log(data, "xxx");
    console.log(query);
    let result: Result = data.find((item: any) => item.route === query) || {};
    console.log(result);
    return result.childs;
}

export function recursiveFind(routeList: Array<string>, data: Array<Object> = bank) {
    console.log(routeList);

    let currentData = findData(routeList.shift(), data);
    console.log(currentData);

    if (routeList.length === 0) return currentData;

    return recursiveFind(routeList, currentData);
}
