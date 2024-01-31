<script lang="ts">
    import { getQuestion } from "$lib/data/fetchData";
    import type { Question } from "$lib/data/types";

    export let questions: Array<string | any>;
    export let next: (correctAmount: number) => void;

    console.log(questions);

    let wrongs: Array<Question> = [];

    let current = 0;
    let correct = 0;
    let question: Question;
    let askWrong = false;
    let trigger = 0;
    $: {
        let _ = trigger + 1;
        question = getQuestion(askWrong ? wrongs[current].id : questions[current]) as Question;
        console.log(current, askWrong, question);
    }
    $: choices = question.shuffle
        ? question.choices.toSorted(() => Math.random() - 0.5)
        : question.choices;

    function clickChoice(choice: string) {
        return (_: any) => {
            if (!askWrong) {
                if (choice == question.answer) {
                    correct++;
                } else {
                    wrongs.push(question);
                    console.log(wrongs);
                }

                if (current == questions.length - 1) {
                    if (wrongs) {
                        current = 0;
                        askWrong = true;
                    } else {
                        next(correct);
                    }
                } else {
                    current++;
                }
            } else {
                if (choice != question.answer) {
                    wrongs.push(question);
                    console.log(wrongs);
                }

                wrongs.shift();

                if (wrongs.length == 0) {
                    next(correct);
                }

                wrongs = wrongs.toSorted(() => Math.random() - 0.5);
            }
        };
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
