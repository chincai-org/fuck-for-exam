<script lang="ts">
    import { goto } from "$app/navigation";
    import Question from "$lib/components/Question.svelte";
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";
    import Button from "$lib/components/Button.svelte";
    import Subjectcard from "$lib/components/Subjectcard.svelte";
    import { auth, firestore } from "$lib/firebase/firebase";
    import { docStore, userStore, User, SignedOut, Doc } from "sveltefire";

    const user = userStore(auth);

    let title = "why lang first";
    let id = "zh";

    const cards = [
        { title: "Sejarah", lastDoneTopic: "12.2" },
        { title: "Math", lastDoneTopic: "2.2" },
        { title: "Science", lastDoneTopic: "1.2" },
        { title: "Sejarah", lastDoneTopic: "12.2" },
        { title: "Math", lastDoneTopic: "2.2" },
        { title: "Science", lastDoneTopic: "1.2" }
    ];
</script>

<SignedOut>
    <p>Please <a href="/login">sign in</a> first</p>
</SignedOut>

<User let:user>
    <Doc ref="users/{user.uid}" let:data>
        <main>
            <p>Hello {data.name}</p>
            <div class="--grid-auto-fit">
                <Subjectcard {cards} />
            </div>
            <Button {title} id={data.language} />
        </main>
    </Doc>
</User>
