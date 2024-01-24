<script lang="ts">
    import type { PageData } from "./$types";
    import Button from "$lib/components/Button.svelte";

    export let data: PageData;

    $: ({ buttons } = data);
    $: ({ id, title } = buttons[0]);
</script>

<main>
    <Button {title} {id} />
</main>
