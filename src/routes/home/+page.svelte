<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import { recursiveFind } from "$lib/data/fetchData";
    import type { Result } from "$lib/data/types";

    let routeList: Array<string> = [];
    $: console.log(routeList);

    $: buttons = recursiveFind(structuredClone(routeList));
    console.log(buttons);
    $: button = buttons[0];
    console.log(button);
    let eventMapping: { [key: string]: (e: any) => void };

    $: {
        eventMapping = {};
        for (let btn of buttons) {
            eventMapping[String(btn.id)] = click(btn);
        }
    }

    function click(btn: Result) {
        return (e: any) => {
            console.log(routeList);
            routeList = [...routeList, btn.route as string];
            console.log(routeList);
            return routeList;
        };
    }

    function changeButton(route: string) {
        console.log("🚀 ~ file: +page.svelte:25 ~ changeButton ~ route:", route);

        console.log(routeList);
        let result = [...routeList, route as string];
        console.log(result);
        return result;
    }

    let question = "hi";

    console.log(buttons);
</script>

<main>
    {#if button.route}
        {#each buttons as button}
            <Button {button} clicked={eventMapping[String(button.id)]} />
        {/each}
    {:else}
        <Question questions={question} />
    {/if}
</main>
