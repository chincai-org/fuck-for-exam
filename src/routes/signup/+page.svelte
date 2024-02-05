<script lang="ts">
    import { createUserWithEmailAndPassword } from "firebase/auth";
    import { doc } from "firebase/firestore";
    import { auth, firestore } from "$lib/firebase/firebase";
    import { signInWithAuth, initiateUser } from "$lib/firebase/utils";

    let name: string;
    let email: string;
    let password: string;
    let cpassword: string;

    let warning: string = "";

    async function signUp() {
        if (name == "") {
            warning = "Please fill in the name";
            return;
        } else if (password != cpassword) {
            warning = "Password does not match";
            return;
        }

        createUserWithEmailAndPassword(auth, email, password)
            .then(async ({ user }) => {
                let docRef = doc(firestore, "users", user.uid);

                await initiateUser(docRef, name);

                window.location.href = "/home";
            })
            .catch(reason => {
                console.log(reason);
                window.location.href = "/";
            });
    }
</script>

<p>{warning}</p>

<div class="--text-center --contact-form">
    <h1 class="--heading-1 --clr-accent-400 --padding-5">FUCK</h1>
    <h3 class="--heading-3">Sign up for Free Unlimited Comprehensive Knowledge</h3>
    <div
        class="form-group --border-radius-1 --margin-inline-15 --margin-block-4 --padding-block-7 --padding-inline-11"
    >
        <button on:click={signInWithAuth} class="--button" data-button="accent">
            <i class="fa-brands fa-google" />Sign up with Google
        </button>
        <input type="text" bind:value={name} placeholder="Username" class="--input" required />
        <input type="text" bind:value={email} placeholder="Enter email" class="--input" required />
        <input
            type="password"
            bind:value={password}
            placeholder="Enter password"
            class="--input"
            required
        />
        <input
            type="password"
            bind:value={cpassword}
            placeholder="Confirm password"
            class="--input"
            required
        />
        <a>Already have an account?</a>
        <button on:click={signUp} class="--button" data-button="accent">Sign in</button>
    </div>
</div>

<style lang="scss">
    @use "/src/lib/sass/abstracts/" as *;
    .--border-radius-1 {
        border: 2px solid $color-neutral-800;
    }

    .form-group * {
        margin: 0.3rem;
    }
</style>
