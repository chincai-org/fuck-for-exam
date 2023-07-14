<script lang="ts">
    import type { PageData } from "./$types";
    import { page } from "$app/stores";

    export let data: PageData;

    console.log(data);

    console.log($page.data.test);
</script>

<main>
    {#each data.buttons as button}
        <a href={window.location.href + "/" + button.route}>{button.title}</a>
        <br />
    {/each}

    <slot />
</main>
