export interface Result {
    id: string;
    title: string;
    childs: Array<Result>;
}

export interface Question {
    id: string;
    questionType: string;
    answerType: string;
    question: string;
    answer: string;
    choices: Array<string>;
    shuffle: boolean;
}

export interface Data {
    name: string;
    language: string;
}
