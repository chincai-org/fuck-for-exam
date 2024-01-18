<script lang="ts">
    import { goto } from "$app/navigation";
    import Buttons from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";
    import Button from "$lib/components/Button.svelte";

    let title = "why lang first";
    let id = "zh";

    const cards = [
        { title: "Sejarah", lastDoneTopic: "12.2" },
        { title: "Math", lastDoneTopic: "2.2" },
        { title: "Science", lastDoneTopic: "1.2" },
        { title: "Sejarah", lastDoneTopic: "12.2" },
        { title: "Math", lastDoneTopic: "2.2" },
        { title: "Science", lastDoneTopic: "1.2" }
    ];
</script>

<main>
    <div class="--grid-auto-fit">
        {#each cards as card}
            <div class="--card">
                <div class="--card__heading">{card.title}</div>
                <hr class="--bg-neutral-1000" />
                <span class="--clr-neutral-500">Continue lesson Topic {card.lastDoneTopic}</span>
            </div>
        {/each}
    </div>
    <Button {title} {id} />
</main>

<style lang="scss">
    hr {
        border: 0;
        border-radius: 100vw;
        height: 2px;
    }
</style>
