<script lang="ts">
    import type { PageData } from "./$types";
    import { goto } from "$app/navigation";

    export let data: PageData;

    function signIn() {
        goto("/login");
    }
</script>

<main class="min-height-100vh">
    <div class="--text-center">
        <h2 class="--heading-2">Welcome to</h2>
        <h1 class="--heading-1 --clr-accent-400">
            FUCK <span class="--clr-neutral-900">for exam</span>
        </h1>
        <h3 class="--heading-3">where you get</h3>
        <h3 class="--heading-3">
            <span class="--clr-accent-400">F</span>ree
            <span class="--clr-accent-400">U</span>nlimited
            <span class="--clr-accent-400">C</span>omprehensive
            <span class="--clr-accent-400">K</span>nowledge
        </h3>
        <h3 class="--heading-3">for exam</h3>
        <div class="--even-columns">
            <button class="--button" data-button="accent">Sign up</button>
            <button on:click={signIn} class="--button" data-button="accent">Login</button>
        </div>
    </div>
</main>

<style>
    .min-height-100vh {
        min-height: 100vh;
    }

    main {
        display: grid;
        place-content: center;
    }

    h1 {
        position: relative;
    }

    h1 > span {
        position: absolute;
        width: max-content;
        bottom: 0.5em;
        right: 11ch;
        rotate: -8deg;
        text-transform: none;
        font-weight: 400;
        font-size: 0.4em;
    }

    button {
        transition: 500ms;
    }
</style>
