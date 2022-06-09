# WEEK 1

## Security Through Obscurity
So, in the cryptography community, security though obscurity means I'm going to make my cryptographic algorithm more secure by just not telling you what it is, and hoping that maybe you don't find out.

**The relationship between system interoperability and cyber security is which of the following?**  Interoperability makes it easier for malicious actors to find and access resources across boundaries.Advancing interoperability certainly does makes security more challenging.

But that's not always the case. For example, as we advance virtualization and cloud, which most Chief Information Security Officers and Chief Information Officers both like. So people who want to propose better computing with cloud and virtualization also are proposing things that are better for security, so it's not always the case that things are at odds.
But with interoperability and security, we have to admit that when we make it easier to do computing, we make it easier to do attacking.

--- 

## **TCP Sequence Number Attack**

what he would do is, as Alice, throw a SYN packet over and watch the SYN/ACK come back. Now, keep in mind, TCP does not do security when it sees a SYN packet. Now, maybe there will be a firewall in between. At that time there wasn't. You throw a SYN, it's throwing you a SYN/ACK. Once you establish a session it might say, "I need a password," all this other stuff. But to just get a packet- A packet responding to basically anybody. So, Alice, Mitnick would go, "Here's a SYN. Watch the SYN/ACK. And let's say it's a hundred. Then here's a SYN, SYN/ACK 200. Again, Christmas Eve. There's not thousands of others doing this. You're the only one. Then here's a SYN. Watch the SYN/ACK 300. You get the idea? 100. 200. 300. 400. Let's say you did that to a thousand. You did it 10 times. You're pretty convinced you know what's coming back. Now, what you do is you send the packet as Bill source IP. You sent it, but the SYN/ACK goes to Bill, but it doesn't matter because you know the SYN/ACK sent 1,100. So, you now ACK with 1,100. And you've got a session set-up.


## what is retrofit.

We didn't design it at conception time. It's sort of like if you're building a house and you want to wire it, let's say you want to put some wires in your home for whatever reason, you don't think Wi-Fi is good enough. You want to put Ethernet. Would it be better to put that in when you're building the house while the walls are still off, or would you want to do it after you've built the whole house and then you overlay? In cyber security, we call that retrofit. 


## reference monitor
Something that sits between two connection and see the traffic coming in or going out. and can make decision about whether allow a traffic or not. (firewall)

**Note** : the first packet in that TCP sequence would have the ACK Bit set to zero. All subsequent packets going back and forth including all data transfer, the ACK that would be set to 1. So now firewall can act on packets that came with ack bit equal to 0. (I beleive this Ack bit was cause the birth of firewall in the early days)


## **Defenition of Firewall**
Basically five things that define a firewall.
1. **it's going to separate two or more networks.** (between network as speration point)

2. it enforces policy. (what it lets through, what it doesn't let through.)

3. some network administrator is going take care of this. It's going to be administrated, but generally by one or the other of the networks (not always, sometimes an ISP might sit in the middle)

4. can't tamper with this thing. So it has to be bullet proof.

5. it can't be bypassed. (The most difficult requirement, the thing has just been almost impossible to deal with)



## Stateful versus Stateless
there is two types of devices, are ones that either have some ability to remember or not, and the thing we're going to remember is something that a computer scientist would refer to as a state.  So a state is something you can think of as like a snapshot.If I want to freeze frame memory in a computer, or freeze frame something, some aspect of memory, just remember it, freeze it and use it in some subsequent state, then that's called being stateful. Like having the ability to capture and use state to have memory, to be able to count something, or say, I saw this before. To have that ability. In contrast, some devices don't do that. Some devices just have programmability that in some sense is referred to as being context-free.

**Statefull Firewall:**  Remember information between states, context-sensitive, more powerfull than stateless.
**Stateless Firewall:**  Not Remember information between states, context-free, less powerfull than statefull.

**Context-free, meaning make the decision, don't worry about what happened previously. Context sensitive, takes a look at what heppened in past.**

