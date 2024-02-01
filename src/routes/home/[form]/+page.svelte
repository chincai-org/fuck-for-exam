<script lang="ts">
    import type { PageData } from "./$types";
    import Button from "$lib/components/Button.svelte";

    export let data: PageData;

    $: ({ buttons } = data);
</script>

<main>
    {#each buttons as button}
        <Button title={button.title} id={button.id} />
    {/each}
</main>
