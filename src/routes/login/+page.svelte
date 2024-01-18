<script lang="ts">
    import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";
    import { doc, setDoc, getDoc } from "firebase/firestore";
    import { auth, firestore } from "$lib/firebase/firebase";

    async function signIn() {
        signInWithPopup(auth, new GoogleAuthProvider()).then(async ({ user }) => {
            let docRef = doc(firestore, "users", user.uid);

            if (!(await getDoc(docRef)).exists())
                await setDoc(
                    docRef,
                    {
                        name: user.displayName,
                        language: "en"
                    },
                    { merge: true }
                );

            window.location.href = "/home";
        });
    }
</script>

<button on:click={signIn}> Sign In </button>
