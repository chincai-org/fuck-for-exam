<script lang="ts">
    import Buttons from "$lib/components/Buttons.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;

    $: buttons = data.buttons;
    $: button = buttons[0];
</script>

<main>
    {#if button.route}
        <Buttons />
    {:else}
        <p>TODO questions</p>
    {/if}

    <slot />
</main>
