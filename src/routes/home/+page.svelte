<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import { recursiveFind } from "$lib/data/fetchData";
    import type { Result } from "$lib/data/types";

    let routeList: Array<string> = [];
    $: console.log(routeList);

    $: buttons = recursiveFind(structuredClone(routeList));
    $: realButtons = buttons as Array<Result>;
    console.log(buttons);
    $: button = buttons[0] as Result;
    console.log(button);
    let eventMapping: { [key: string]: (e: any) => void };

    $: {
        eventMapping = {};
        for (let btn of buttons as Array<Result>) {
            eventMapping[btn.id as string] = click(btn);
        }
    }

    function click(btn: Result) {
        return (e: any) => {
            console.log(routeList);
            routeList = [...routeList, btn.id as string];
            console.log(routeList);
            return routeList;
        };
    }
    console.log(buttons);
</script>

<main>
<<<<<<< HEAD
    {#if button.route}
        {#each buttons as button}
            <Button {button} clicked={eventMapping[String(button.id)]} />
        {/each}
    {:else}
        <Question questions={question} />
=======
    {#if button.id}
        {#each buttons as realButtons}
            <Button {button} clicked={eventMapping[button.id]} />
        {/each}
    {:else}
        <Question questions={buttons} />
>>>>>>> 44ee973c611a4c1542f1c96cb835917939757cd2
    {/if}
</main>

<style lang="sass">
    main
        background-color: black
</style>
