<script lang="ts">
    import Buttons from "$lib/components/Buttons.svelte";
    import Question from "$lib/components/Question.svelte";
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";

    export let data: PageData;

    let buttons: any, button: any;

    $: buttons = data.buttons;
    $: button = buttons[0];

    console.log(buttons);
</script>

<main>
    {#if button.route}
        <Buttons {buttons} />
    {:else}
        <Question />
    {/if}

    <slot />
</main>
