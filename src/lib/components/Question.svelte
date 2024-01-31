<script lang="ts">
    import { getQuestion } from "$lib/data/fetchData";
    import type { Question } from "$lib/data/types";

    export let questions: Array<string | any>;
    export let next: (correctAmount: number) => void;

    console.log(questions);

    let wrongs: Array<Question> = [];

    let current = 0;
    let correctAmount = 0;
    let question: Question;
    let askWrong = false;
    let answered = false;
    let correct = false;
    $: {
        question = getQuestion(askWrong ? wrongs[current].id : questions[current]) as Question;
        console.log(current, askWrong, question);
    }
    $: choices = question.shuffle
        ? question.choices.toSorted(() => Math.random() - 0.5)
        : question.choices;

    function validate(choice: string) {
        if (!askWrong) {
            if (choice == question.answer) {
                correct = true;
                correctAmount++;
            } else {
                correct = false;
                wrongs.push(question);
            }
        } else {
            if (choice != question.answer) {
                correct = false;
                wrongs.push(question);
            } else {
                correct = true;
            }

            wrongs.shift();
        }
    }

    function clickChoice(choice: string) {
        return (_: any) => {
            validate(choice);
            answered = true;
        };
    }

    function nextQuestion() {
        if (!askWrong) {
            if (current == questions.length - 1) {
                if (wrongs.length > 0) {
                    current = 0;
                    askWrong = true;
                } else {
                    next(correctAmount);
                }
            } else {
                current++;
            }
        } else {
            if (wrongs.length == 0) {
                next(correctAmount);
            }

            wrongs = wrongs.toSorted(() => Math.random() - 0.5);
        }

        answered = false;
    }
</script>

{#if askWrong}
    Previous mistake
{/if}

{#if question.questionType == "vocab"}
    <p>What is the definition of the following word?</p>
{/if}

<p>{question.question}</p>

{#if question.answerType == "objective"}
    {#each choices as choice}
        <button on:click={clickChoice(choice)}>{choice}</button>
    {/each}
{/if}

{#if answered}
    <div>
        <p>{correct ? "Correct" : "Wrong"}</p>
        {#if !correct}
            <p>Correct: {question.answer}</p>
        {/if}
        <button on:click={nextQuestion}>Next question</button>
    </div>
{/if}
