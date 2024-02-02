<script lang="ts">
    import Question from "$lib/components/Question.svelte";
    import Stats from "$lib/components/Stats.svelte";
    import { page } from "$app/stores";

    import { userStore, docStore, collectionStore } from "sveltefire";
    import { auth, firestore } from "$lib/firebase/firebase";
    import { doc, addDoc, getDoc, updateDoc, collection } from "firebase/firestore";
    import type { Data } from "$lib/data/types";

    export let data: any;

    const user = userStore(auth);
    const userData = docStore<Data>(firestore, `users/${$user?.uid}`);
    const path = "/" + $page.url.pathname.split("/").slice(2, -1).join("/");

    console.log($user?.uid);

    $: ({ buttons } = data);

    const start = Date.now();
    let score: number;
    let timeLapse: number;

    async function updateHistory() {
        const language = $userData?.language as string;
        const history = $userData?.history[language] as Array<string>;
        console.log(history);

        const index = history.indexOf(path);

        if (index !== -1) {
            // If path exists, move it to the front
            const updatedHistory = [path, ...history.slice(0, index), ...history.slice(index + 1)];
            await updateDoc(doc(firestore, "users", $user?.uid as string), {
                history: {
                    [language]: updatedHistory
                }
            });
        } else {
            // If path doesn't exist, append it to the front
            const updatedHistory = [path, ...history];
            await updateDoc(doc(firestore, "users", $user?.uid as string), {
                history: {
                    [language]: updatedHistory
                }
            });
        }
    }

    function next(_score: number) {
        score = _score;
        timeLapse = Date.now() - start;

        updateHistory();
    }

    console.log($page.url.pathname);
</script>

<main>
    {#if score == undefined}
        <Question questions={buttons} {next} />
    {:else}
        <Stats {score} timeInMilliseconds={timeLapse} />
    {/if}
</main>
