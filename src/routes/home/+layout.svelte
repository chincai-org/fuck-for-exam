<script lang="ts">
    // import type { LayoutData } from "./$types";
    import { page } from "$app/stores";
    import Buttons from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import "/src/lib/sass/main.scss";
    import { onNavigate } from "$app/navigation";

    // export let data: LayoutData;

    onNavigate(navigation => {
        //@ts-ignore
        if (!document.startViewTransition) return;

        return new Promise(resolve => {
            //@ts-ignore
            document.startViewTransition(async () => {
                resolve();
                await navigation.complete;
            });
        });
    });

    const navigations = [
        { title: "Home", path: "/home", icon: "fa-solid fa-house" },
        { title: "Settings", path: "/home/setting", icon: "fa-solid fa-gear" },
        { title: "Quest", path: "/home/quest", icon: "" },
        { title: "Leaderboard", path: "/home/leaderboard", icon: "" }
    ];
</script>

<main class="--bg-neutral-100">
    <nav>
        <ul class="--nav">
            {#each navigations as navigation}
                <li class:active={$page.url.pathname === navigation.path}>
                    <i class={navigation.icon} />
                    <a href={navigation.path}>{navigation.title}</a>
                </li>
            {/each}
        </ul>
    </nav>
    <slot />
</main>

<style lang="scss">
    @use "/src/lib/sass/abstracts/" as *;

    main {
        min-height: 100vh;
        display: grid;
        grid-template-columns: 18rem 1fr;
        gap: 2rem;
    }

    nav {
        background: $color-neutral-200;
        top: 0;
        bottom: 0;
        left: 0;
        max-height: 100svh;
        position: sticky;
        padding-block: 2rem;
    }

    ul {
        li {
            display: grid;
            padding-block: 1rem;
            padding-inline: 2rem;
            margin-inline: 1rem 0;
            box-shadow: 2px 0 0 $color-neutral-100;
            grid-template-columns: 3rem 1fr;

            &.active {
                $border-radius: 3rem;

                view-transition-name: navigation;
                background-color: $color-neutral-100;
                position: relative;
                z-index: -1;
                border-radius: 100vw 0 0 100vw;

                @include before-after($locations: before after, $right: 0) {
                    width: $border-radius;
                    height: $border-radius;
                    background: $color-neutral-200;
                }

                @include before-after($locations: before, $top: $border-radius * -1) {
                    border-radius: 0 0 $border-radius;
                    box-shadow: calc($border-radius / 6) calc($border-radius / 6) 0
                        calc($border-radius / 6) $color-neutral-100;
                }

                @include before-after($locations: after, $bottom: $border-radius * -1) {
                    border-radius: 0 $border-radius 0 0;
                    box-shadow: calc($border-radius / 6) calc(($border-radius / -6)) 0
                        calc($border-radius / 6) $color-neutral-100;
                }
            }

            @for $i from 1 through 4 {
                &:nth-child(#{$i}) a {
                    view-transition-name: navLink-#{$i};
                }
                &:nth-child(#{$i}) i {
                    view-transition-name: navIcon-#{$i};
                }
            }
        }
    }
</style>
