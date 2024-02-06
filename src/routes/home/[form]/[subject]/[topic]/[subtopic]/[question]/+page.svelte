<script lang="ts">
    import Question from "$lib/components/Question.svelte";
    import Stats from "$lib/components/Stats.svelte";
    import Streak from "$lib/components/Streak.svelte";
    import { page } from "$app/stores";

    import { userStore, docStore } from "sveltefire";
    import { auth, firestore } from "$lib/firebase/firebase";
    import { doc, updateDoc, increment, Timestamp } from "firebase/firestore";
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
    let fsm = 0; // Finite state machine
    let streak: number;

    let streakUpdated: boolean;

    $: if (fsm == 3) {
        // TODO go back
        console.log("BACK");
    }

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

    async function updateStreak() {
        streak = $userData?.streak as number;

        const lastDate = $userData?.lastDay.toDate() as Date;
        const today = new Date();

        if (differExactlyOneDay(lastDate, today)) {
            streak++;

            await updateDoc(doc(firestore, "users", $user?.uid as string), {
                streak: increment(1),
                lastDay: Timestamp.fromDate(today)
            });

            return true;
        }

        return false;
    }

    function differExactlyOneDay(date1: Date, date2: Date): boolean {
        // Get the year, month, and day of each date
        const year1 = date1.getFullYear();
        const month1 = date1.getMonth();
        const day1 = date1.getDate();

        const year2 = date2.getFullYear();
        const month2 = date2.getMonth();
        const day2 = date2.getDate();

        // Calculate the difference in days
        const differenceDays =
            Math.abs(Date.UTC(year1, month1, day1) - Date.UTC(year2, month2, day2)) /
            (1000 * 60 * 60 * 24);

        // Check if the difference is exactly one day
        return differenceDays === 1;
    }

    function questionNext(_score: number) {
        score = _score;
        timeLapse = Date.now() - start;

        fsmNext();

        updateHistory();
        updateStreak().then(_streakUpdated => (streakUpdated = _streakUpdated));
    }

    function statsNext() {
        if (streakUpdated) {
            fsmNext();
        } else {
            fsmNext(3);
        }
    }

    function fsmNext(n: number = -1) {
        fsm = n == -1 ? fsm + 1 : n;
        console.log(fsm);
    }
</script>

<main>
    {#if fsm == 0}
        <Question questions={buttons} next={questionNext} />
    {:else if fsm == 1}
        <Stats {score} timeInMilliseconds={timeLapse} next={statsNext} />
    {:else if fsm == 2}
        <Streak {streak} />
    {/if}
</main>
