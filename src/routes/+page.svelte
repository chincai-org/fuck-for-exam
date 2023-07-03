<script src="ts">
    import { collection, addDoc } from "firebase/firestore";
    import { db } from "$lib/firebase/firebase";

    let num = 0;

    async function add() {
        await addDoc(collection(db, "test"), {
            num: num
        });
        num++;
    }
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<button on:click={add}>Inserted {num} docs</button>
