<script lang="ts">
    import { signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
    import { doc, setDoc, getDoc } from "firebase/firestore";
    import { auth, firestore } from "$lib/firebase/firebase";

    let email: string;
    let password: string;

    function signIn() {
        signInWithEmailAndPassword(auth, email, password)
            .then(() => {
                window.location.href = "/home";
            })
            .catch(reason => {
                console.log(reason);
                window.location.href = "/";
            });
    }

    async function signInWithAuth() {
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

<input type="text" bind:value={email} placeholder="Enter email" />
<input type="password" bind:value={password} placeholder="Enter password" />
<button on:click={signIn}>Sign in</button>

<button on:click={signInWithAuth}>Sign in with Google</button>
