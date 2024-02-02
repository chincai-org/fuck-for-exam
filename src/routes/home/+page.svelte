<script lang="ts">
    import { goto } from "$app/navigation";
    import Question from "$lib/components/Question.svelte";
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";
    import Button from "$lib/components/Button.svelte";
    import Subjectcard from "$lib/components/Subjectcard.svelte";
    import LinkHandler from "$lib/components/LinkHandler.svelte";
    import Logger from "$lib/components/Logger.svelte";
    import { auth, firestore } from "$lib/firebase/firebase";
    import { userStore, User, Doc } from "sveltefire";
    import { recursiveFind } from "$lib/data/fetchData";
    import type { Result } from "$lib/data/types";

    function find(lang: string) {
        return recursiveFind([lang]) as Result[];
    }
</script>

<User let:user>
    <Doc ref="users/{user.uid}" let:data>
        <main>
            {#each data.history[data.language] as link}
                <LinkHandler {link} language={data.language} let:subject let:subChapter>
                    <Subjectcard lessonLink={link} title={subject} lastDoneTopic={subChapter} />
                </LinkHandler>
            {/each}

            {#each find(data.language) as button}
                <Button title={button.title} id={button.id} />
            {/each}

            <!-- <Subjectcard {card} /> -->
        </main>
    </Doc>
</User>
