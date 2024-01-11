<script lang="ts">
    import Question from "$lib/components/Question.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;

    $: ({ buttons } = data);
</script>

<main>
    <Question questions={buttons} />
</main>
