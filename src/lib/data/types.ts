export interface Result {
    id: string;
    title: string;
    childs: Array<Result>;
}

export interface Question {
    questionType: string;
    answerType: string;
    question: string;
    answer: string;
    choices: Array<string>;
}
