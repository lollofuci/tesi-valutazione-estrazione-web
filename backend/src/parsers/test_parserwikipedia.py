import asyncio

from parsers.wikipedia_parser import WikipediaParser


async def main():
    parser = WikipediaParser()
    result = await parser.parse("https://it.wikipedia.org/wiki/Avellino")

    print("\nTITLE:")
    print(result["title"])

    print("\nDOMAIN:")
    print(result["domain"])

    print("\nHTML TEXT PREVIEW:")
    print(result["html_text"][:])

    print("\nPARSED TEXT PREVIEW:")
    print(result["parsed_text"][:])

    print("\nLUNGHEZZE:")
    print(f'html_text: {len(result["html_text"])} caratteri')
    print(f'parsed_text: {len(result["parsed_text"])} caratteri')


if __name__ == "__main__":
    asyncio.run(main())