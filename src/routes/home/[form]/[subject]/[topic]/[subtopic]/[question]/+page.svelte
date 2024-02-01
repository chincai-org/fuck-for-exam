<script lang="ts">
    import Question from "$lib/components/Question.svelte";
    import Stats from "$lib/components/Stats.svelte";

    export let data: any;

    $: ({ buttons } = data);

    const start = Date.now();
    let score: number;
    let timeLapse: number;

    function next(_score: number) {
        score = _score;
        timeLapse = Date.now() - start;
    }
</script>

<main>
    {#if score == undefined}
        <Question questions={buttons} {next} />
    {:else}
        <Stats {score} timeInMilliseconds={timeLapse} />
    {/if}
</main>
