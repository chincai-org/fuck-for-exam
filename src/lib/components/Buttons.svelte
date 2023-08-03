<script lang="ts">
    import { page } from "$app/stores";
</script>

{#each $page.data.buttons as button}
    <a href={window.location.href + "/" + button.route}>{button.title}</a>
    <br />
{/each}
