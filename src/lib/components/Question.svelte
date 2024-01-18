<script lang="ts">
    import { getQuestion } from "$lib/data/fetchData";
    import type { Question } from "$lib/data/types";

    export let questions: Array<string | any>;

    console.log(questions);
        
    let current = 0;
    let question: Question;
    $: question = getQuestion(questions[current]);
</script>

{#if question.questionType == "vocab"}
    <p>What is the definition of the following word?</p>
{/if}

<p>{question.question}</p>

{#if question.answerType == "objective"}
    {#each question.choices as choice}
        <button>{choice}</button>
    {/each}
{/if}
