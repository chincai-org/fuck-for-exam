<script lang="ts">
    // import type { LayoutData } from "./$types";
    import { page } from "$app/stores";
    import Buttons from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import "/src/app.scss";
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
        { title: "Setting", path: "/home/setting", icon: "fa-solid fa-gear" },
        { title: "Quest", path: "/home/quest", icon: "" },
        { title: "Leaderboard", path: "/home/leaderboard", icon: "" }
    ];
</script>

<main>
    <nav>
        <ul>
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
    @use "/src/lib/sass/theme/colour.scss" as *;
    @use "/src/lib/sass/theme/mixin.scss" as *;

    main {
        min-height: 100vh;
        display: grid;
        grid-template-columns: 18rem 1fr;
        gap: 2rem;
    }

    nav {
        background: $home-sidebar-navigation-background-colour;
        top: 0;
        bottom: 0;
        left: 0;
        max-height: 100svh;
        position: sticky;
        padding-block: 2rem;
    }

    ul {
        margin: 0;
        padding: 0;
        list-style: none;
        display: grid;
        gap: 1rem;
        font-size: 1.7rem;

        li {
            display: grid;
            padding-block: 1rem;
            padding-inline: 2rem;
            margin-inline: 1rem 0;
            box-shadow: 2px 0 0 $default-darktheme-background-colour;
            grid-template-columns: 3rem 1fr;

            &.active {
                $border-radius: 3rem;

                view-transition-name: navigation;
                background-color: $default-darktheme-background-colour;
                position: relative;
                z-index: -1;
                border-radius: 100vw 0 0 100vw;

                @include before-after($locations: before after, $right: 0) {
                    width: $border-radius;
                    height: $border-radius;
                    background: $home-sidebar-navigation-background-colour;
                }

                @include before-after($locations: before, $top: $border-radius * -1) {
                    border-radius: 0 0 $border-radius;
                    box-shadow: ($border-radius / 6) ($border-radius / 6) 0 ($border-radius / 6)
                        $default-darktheme-background-colour;
                }

                @include before-after($locations: after, $bottom: $border-radius * -1) {
                    border-radius: 0 $border-radius 0 0;
                    box-shadow: ($border-radius / 6) (-($border-radius / 6)) 0 ($border-radius / 6)
                        $default-darktheme-background-colour;
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

        a,
        i {
            @include change-default($color: white);
            display: block;

            &:hover {
                color: rgb(192, 192, 192);
            }
        }
    }
</style>
