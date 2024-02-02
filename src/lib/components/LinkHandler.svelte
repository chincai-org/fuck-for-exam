<script lang="ts">
    import { recursiveFind, findData } from "$lib/data/fetchData";
    import type { Result } from "$lib/data/types";

    export let link: string;
    export let language: string;

    console.log(link);

    const routeList = link.split("/").toSpliced(0, 1);
    console.log(routeList);
    const subject = (
        recursiveFind([language, routeList[0]]).find(
            (item: any) => item.id === routeList[1]
        ) as Result
    ).title;

    console.log(routeList.slice(0, -1));
    console.log(routeList[-1]);
    const subChapter = (
        recursiveFind([language, ...routeList.slice(0, -1)]).find(
            (item: any) => item.id === routeList.at(-1)
        ) as Result
    ).title;
</script>

<slot {subject} {subChapter} />
