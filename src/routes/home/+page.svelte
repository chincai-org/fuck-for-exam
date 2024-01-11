<script lang="ts">
    import { goto } from "$app/navigation";
    import Buttons from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";
    import Button from "$lib/components/Button.svelte";

    let title = "never gonna give you up";
    let id = "zh";
</script>

<main>
    <Button {title} {id} />
</main>
