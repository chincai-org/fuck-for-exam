<script lang="ts">
    import { goto } from "$app/navigation";
    import Buttons from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";
    import Button from "$lib/components/Button.svelte";

    export let data: PageData;
    console.log(data);
    let buttons: any, button: any;

    $: buttons = data.buttons;
    $: ({ id, title, child } = buttons[0]);

    $: console.log(id, title);
</script>

<main>
    <Button {title} {id} />
</main>
