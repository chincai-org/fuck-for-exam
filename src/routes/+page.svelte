<script lang="ts">
    import { collection, addDoc } from "firebase/firestore";
    import { db } from "$lib/firebase/firebase";
    import { getDefinition } from "$lib/data/fetchData";

    let num = 0;
    let route: string = "/";

    async function add() {
        await addDoc(collection(db, "test"), {
            num: num
        });
        num++;
    }

    console.log(getDefinition("ZH", "wilayah"));
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<button on:click={add}>Inserted {num} docs</button>

<input type="text" bind:value={route} />
<a href={route}>Go to route</a>
