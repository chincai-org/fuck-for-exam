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
        { title: "Setting", path: "/home/setting", icon: "fa-solid fa-gear" }
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
    $sidebar-navigation-background-colour: rgb(46, 46, 49);
    $active-colour: rgb(29, 29, 32);

    main {
        min-height: 200vh;
        display: grid;
        grid-template-columns: 17rem 1fr;
        gap: 2rem;
    }

    nav {
        background: $sidebar-navigation-background-colour;
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
            box-shadow: 2px 0 0 $active-colour;
            grid-template-columns: 3rem 1fr;

            &.active {
                $border-radius: 3rem;

                view-transition-name: navigation;
                background-color: $active-colour;
                position: relative;
                z-index: -1;
                border-radius: 100vw 0 0 100vw;

                &::before,
                &::after {
                    content: "";
                    position: absolute;
                    width: $border-radius;
                    height: $border-radius;
                    right: 0rem;
                    background: $sidebar-navigation-background-colour;
                }

                &::before {
                    border-radius: 0 0 $border-radius;
                    top: $border-radius * -1;
                    box-shadow: 8px 8px 0 8px $active-colour;
                }

                &::after {
                    border-radius: 0 $border-radius 0 0;
                    bottom: $border-radius * -1;
                    box-shadow: 8px -8px 0 8px $active-colour;
                }
            }
            @for $i from 1 through 2 {
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
            user-select: none;
            color: white;
            text-decoration: none;
            display: block;

            &:hover {
                color: rgb(192, 192, 192);
            }
        }
    }
</style>
