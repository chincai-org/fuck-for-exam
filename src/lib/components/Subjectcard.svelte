<script lang="ts">
    export let cards: any;
</script>

{#each cards as card}
    <div class="--card">
        <h1 class="--card__heading">{card.title}</h1>
        <hr class="--bg-neutral-1000" />
        <span class="--clr-neutral-500">Continue lesson Topic {card.lastDoneTopic}</span>
    </div>
{/each}

<style lang="scss">
    hr {
        border: 0;
        border-radius: 100vw;
        height: 2px;
    }
</style>
