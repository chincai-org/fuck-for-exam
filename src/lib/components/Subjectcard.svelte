<script lang="ts">
    import { goto } from "$app/navigation";

    export let title: string;
    export let lastDoneTopic: string;
    export let lessonLink: string;

    function teleport(e: any) {
        goto("/home" + lessonLink);
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="--grid-auto-fit" on:click={teleport}>
    <div class="--card">
        <h1 class="--card__heading">{title}</h1>
        <hr class="--bg-neutral-1000" />
        <span class="--clr-neutral-500">Continue lesson Topic {lastDoneTopic}</span>
    </div>
</div>

<style lang="scss">
    hr {
        border: 0;
        border-radius: 100vw;
        height: 2px;
    }
</style>
