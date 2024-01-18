<script lang="ts">
    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<main class="min-height-100vh">
    <div class="--text-center">
        <h2 class="--heading-2">Welcome to</h2>
        <h1 class="--heading-1">FUCK</h1>
        <h3 class="--heading-3">where you get</h3>
        <h3 class="--heading-3">
            <span class="--clr-accent-400">F</span>ree
            <span class="--clr-accent-400">U</span>nlimited
            <span class="--clr-accent-400">C</span>omprehensive
            <span class="--clr-accent-400">K</span>nowledge
        </h3>
        <div class="--even-columns">
            <button class="--button" data-button="accent">Sign up</button>
            <a href="/login"><button class="--button" data-button="accent">Login</button></a>
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
</style>
