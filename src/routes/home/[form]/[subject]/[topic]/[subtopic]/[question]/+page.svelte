<script lang="ts">
    import Question from "$lib/components/Question.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;

    $: ({ buttons } = data);

    function next(correct: boolean) {}
</script>

<main>
    <Question questions={buttons} {next} />
</main>
