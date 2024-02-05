<script lang="ts">
    import { signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
    import { auth } from "$lib/firebase/firebase";
    import { signInWithAuth } from "$lib/firebase/utils";

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
</script>

<div class="--text-center --contact-form">
    <h1 class="--heading-1 --clr-accent-400 --padding-1">FUCK</h1>
    <h3 class="--heading-3">Sign in an existing account</h3>
    <div class="form-group --border-radius-1 --margin-inline-15 --margin-block-5 --padding-11">
        <button on:click={signInWithAuth} class="--button" data-button="accent">
            <i class="fa-brands fa-google" />Sign in with Google
        </button>
        <input type="text" bind:value={email} placeholder="Enter email" class="--input" />
        <input type="password" bind:value={password} placeholder="Enter password" class="--input" />
        <a>Forgot your password?</a>
        <button on:click={signIn} class="--button" data-button="accent">Sign in</button>
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
