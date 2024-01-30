<script lang="ts">
    import { getQuestion } from "$lib/data/fetchData";
    import type { Question } from "$lib/data/types";
    import { writable } from "svelte/store";

    export let questions: Array<string | any>;
    export let next: (correct: boolean) => void;

    console.log(questions);

    let current = 0;
    let correct = 0;
    let question: Question;
    $: question = getQuestion(questions[current]);

    function clickChoice(choice: string) {
        return (e: any) => {
            if (choice == question.answer) {
                correct++;
            }

            current++;
        };
    }
</script>

{#if question.questionType == "vocab"}
    <p>What is the definition of the following word?</p>
{/if}

<p>{question.question}</p>

{#if question.answerType == "objective"}
    {#each question.choices as choice}
        <button on:click={clickChoice(choice)}>{choice}</button>
    {/each}
{/if}
