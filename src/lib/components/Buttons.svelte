<script lang="ts">
    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import Button from "./Button.svelte";

    export let buttons: any;

    onMount(() => {
        console.log("Hello");
    });
</script>

{#each buttons as button}
    <Button {button} />
    <br />
{/each}
